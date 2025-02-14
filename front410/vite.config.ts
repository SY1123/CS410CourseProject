import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import styleImport, {AntdResolve} from 'vite-plugin-style-import'

// https://vitejs.dev/config/
export default defineConfig({
  css: {
    preprocessorOptions: {
      less: {
        javascriptEnabled: true,
        additionalData: '@root-entry-name: default;',
      },
    },
  },
  plugins: [
    react(),
    styleImport({
      resolves: [
        AntdResolve()
      ]
    }),
  ]
})
