import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'
import { createHtmlPlugin } from 'vite-plugin-html'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    createHtmlPlugin({
      inject:{
        data:{
          title: 'MyMyst - Organize your lists easily',
          description: 'MyMyst is a web application that allows you to create and manage lists of items. It is designed to be simple and easy to use, while also providing powerful features to help you stay organized.',
          ogImage: 'https://mymyst.app/og-image.jpg',
        }
      }
    }),
    tailwindcss(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
