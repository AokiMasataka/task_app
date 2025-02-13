import vue from 'npm:@vitejs/plugin-vue@^5.0.4'
import Vuetify, { transformAssetUrls } from 'npm:vite-plugin-vuetify'
import { defineConfig } from 'npm:vite@^5.2.10'
import 'npm:vue@^3.4.23'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue({template: { transformAssetUrls },}),
        Vuetify()
    ],
    css: {
        preprocessorOptions: {
            css: { charset: false }
        }
    },
    server: {
        port: 3000,
    },
})
