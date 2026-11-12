(function (root) {
  "use strict";
  const profiles = [
    {
      id: "enzo",
      name: "Enzo",
      age: 26,
      city: "São Paulo, SP",
      height: 1.84,
      categories: ["Fashion", "Editorial", "Comercial"],
      photoHeight: 63,
    },
    {
      id: "gabriel",
      name: "Gabriel",
      age: 28,
      city: "Rio de Janeiro, RJ",
      categories: [],
      photoHeight: 63,
    },
    {
      id: "rafael",
      name: "Rafael",
      age: 29,
      city: "São Paulo, SP",
      categories: [],
      photoHeight: 65,
    },
    {
      id: "theo",
      name: "Theo",
      age: 24,
      city: "Belo Horizonte, MG",
      categories: [],
      photoHeight: 65,
    },
  ];
  const castings = [
    {
      id: "campanha-inverno-2025",
      title: "Campanha Inverno 2025",
      city: "São Paulo, SP",
      date: "18 de mar de 2025",
      tags: ["Moda", "Editorial"],
      fee: "Cachê sob consulta",
      photo: "campanha-inverno-2025.png",
    },
    {
      id: "marca-esportiva",
      title: "Marca Esportiva",
      city: "Rio de Janeiro, RJ",
      date: "25 de mar de 2025",
      tags: ["Fitness", "Comercial"],
      fee: "R$ 1.200 - R$ 2.000",
      feeRange: [1200, 2000],
      photo: "marca-esportiva.png",
    },
    {
      id: "editorial-masculino",
      title: "Editorial Masculino",
      city: "São Paulo, SP",
      date: "30 de mar de 2025",
      tags: ["Editorial", "Lifestyle"],
      fee: "R$ 800 - R$ 1.500",
      feeRange: [800, 1500],
      photo: "editorial-masculino.png",
    },
  ];
  const data = { profiles, castings };
  root.ModelData = data;
  if (typeof module !== "undefined") module.exports = data;
})(typeof window === "undefined" ? globalThis : window);
