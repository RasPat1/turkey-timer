/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: ['templates/*.html', './src/**/*.{html,js}', './node_modules/tw-elements/dist/js/**/*.js'],
  presets: [],
  darkMode: 'media', // or 'class'
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    }
  },
  plugins: [
    require('tw-elements/dist/plugin')
  ]
}
