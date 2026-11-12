const {defineConfig}=require('@playwright/test');
module.exports=defineConfig({testDir:'./tests/e2e',use:{baseURL:'http://127.0.0.1:8878',browserName:'chromium',launchOptions:{executablePath:'/usr/bin/chromium'}},webServer:{command:'python3 -m http.server 8878 --bind 127.0.0.1',port:8878,reuseExistingServer:true}});
