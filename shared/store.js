(function (root) {
  "use strict";
  const data =
    root.ModelData ||
    (typeof require === "function" ? require("./data.js") : null);
  const key = "model:state:v1";
  const defaults = () => ({
    schemaVersion: 1,
    savedProfileIds: data.profiles.map((x) => x.id),
    savedCastingIds: [],
    likedProfileIds: [],
    dismissedProfileIds: [],
    filters: {
      applied: false,
      origin: "castings",
      city: "São Paulo, SP",
      distance: "50",
      age: [18, 35],
      height: [1.7, 1.95],
      fee: [300, 5000],
      categories: ["Fashion"],
      availability: "Imediata",
    },
    profile: {
      name: "Matheus Silva",
      age: "24",
      city: "São Paulo, SP",
      height: "1,85 m",
      weight: "80 kg",
      size: "42",
      availability: "Não informada",
    },
    messages: [],
    notificationReadStates: Array(6).fill(null),
  });
  const clone = (x) => JSON.parse(JSON.stringify(x));
  function normalize(raw) {
    const d = defaults();
    if (!raw || raw.schemaVersion !== 1) return d;
    for (const [field, valid] of [
      ["savedProfileIds", data.profiles],
      ["likedProfileIds", data.profiles],
      ["dismissedProfileIds", data.profiles],
      ["savedCastingIds", data.castings],
    ])
      if (Array.isArray(raw[field]))
        d[field] = [
          ...new Set(raw[field].filter((id) => valid.some((x) => x.id === id))),
        ];
    if (
      raw.filters &&
      typeof raw.filters === "object" &&
      !Array.isArray(raw.filters)
    ) {
      const f = raw.filters;
      if (typeof f.city === "string") d.filters.city = f.city.slice(0, 100);
      if (["10", "25", "50", "100"].includes(f.distance))
        d.filters.distance = f.distance;
      if (
        ["", "Imediata", "Próximas semanas", "Flexível"].includes(
          f.availability,
        )
      )
        d.filters.availability = f.availability;
      if (["descobrir", "castings"].includes(f.origin))
        d.filters.origin = f.origin;
      d.filters.applied = f.applied === true;
      for (const k of ["age", "height", "fee"])
        if (
          Array.isArray(f[k]) &&
          f[k].length === 2 &&
          f[k].every(Number.isFinite) &&
          f[k][0] <= f[k][1] &&
          f[k][0] >= { age: 18, height: 1, fee: 0 }[k] &&
          f[k][1] <= { age: 100, height: 2.5, fee: 100000 }[k]
        )
          d.filters[k] = f[k];
      if (Array.isArray(f.categories))
        d.filters.categories = f.categories.filter((x) =>
          [
            "Fashion",
            "Fitness",
            "Comercial",
            "Editorial",
            "Lifestyle",
            "Passarela",
          ].includes(x),
        );
    }
    if (
      raw.profile &&
      typeof raw.profile === "object" &&
      !Array.isArray(raw.profile)
    )
      for (const k of Object.keys(d.profile))
        if (
          typeof raw.profile[k] === "string" &&
          raw.profile[k].trim() &&
          (k !== "age" ||
            (/^[0-9]+$/.test(raw.profile[k]) &&
              +raw.profile[k] >= 18 &&
              +raw.profile[k] <= 100)) &&
          (k !== "availability" ||
            ["Não informada", "Disponível", "Indisponível"].includes(
              raw.profile[k],
            ))
        )
          d.profile[k] = raw.profile[k].slice(0, 100);
    if (Array.isArray(raw.messages))
      d.messages = raw.messages
        .filter((x) => x && typeof x.text === "string")
        .map((x) => ({ text: x.text.slice(0, 5000) }));
    if (Array.isArray(raw.notificationReadStates))
      d.notificationReadStates = d.notificationReadStates.map((_, i) =>
        ["lida", "não lida"].includes(raw.notificationReadStates[i])
          ? raw.notificationReadStates[i]
          : null,
      );
    return d;
  }
  let storageAvailable = true;
  function read() {
    try {
      const value = root.localStorage && root.localStorage.getItem(key);
      return value ? normalize(JSON.parse(value)) : defaults();
    } catch (e) {
      storageAvailable = false;
      return defaults();
    }
  }
  let state = read();
  const listeners = new Set();
  function dispatch(action) {
    const next = clone(state);
    switch (action.type) {
      case "toggle": {
        if (
          ![
            "savedProfileIds",
            "savedCastingIds",
            "likedProfileIds",
            "dismissedProfileIds",
          ].includes(action.field)
        )
          return;
        const ids = next[action.field];
        const index = ids.indexOf(action.id);
        if (index < 0) ids.push(action.id);
        else ids.splice(index, 1);
        break;
      }
      case "filters":
        next.filters = { ...next.filters, ...action.value };
        break;
      case "profile":
        next.profile = { ...next.profile, ...action.value };
        break;
      case "message":
        next.messages.push({ text: action.text });
        break;
      case "notifications":
        next.notificationReadStates = action.value;
        break;
      default:
        return;
    }
    state = normalize(next);
    try {
      root.localStorage.setItem(key, JSON.stringify(state));
      storageAvailable = true;
    } catch (e) {
      storageAvailable = false;
    }
    listeners.forEach((fn) => fn(clone(state)));
    return { persistent: storageAvailable };
  }
  const api = {
    getState: () => clone(state),
    dispatch,
    subscribe(fn) {
      listeners.add(fn);
      return () => listeners.delete(fn);
    },
    isPersistent: () => storageAvailable,
  };
  if (root.addEventListener)
    root.addEventListener("storage", (event) => {
      if (event.key === key) {
        try {
          state = event.newValue
            ? normalize(JSON.parse(event.newValue))
            : defaults();
        } catch (e) {
          state = defaults();
        }
        listeners.forEach((fn) => fn(clone(state)));
      }
    });
  root.ModelStore = api;
  if (typeof module !== "undefined") module.exports = api;
})(typeof window === "undefined" ? globalThis : window);
