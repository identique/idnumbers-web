import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { createHtmlPlugin } from 'vite-plugin-html'
import path from 'path'


// https://vitejs.dev/config/
export default defineConfig({
  build:{
    outDir: "../templates",
    emptyOutDir: false,
    copyPublicDir: false,
    rollupOptions: {
      output:{
        entryFileNames: 'static/[name]-[hash].js',
        chunkFileNames: 'static/[name]-[hash].js',
        assetFileNames: 'static/[name]-[hash][extname]'
      },
      watch: {
        include: 'src/**',
        exclude: 'node_modules/**'
      }
    }
  },
  plugins: [
    react()
  ]
})
