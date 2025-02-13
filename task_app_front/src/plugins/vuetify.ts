/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
// import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'
import { VDateInput } from 'vuetify/labs/VDateInput'
import colors from 'vuetify/util/colors'

export default createVuetify({
  locale: {
    locale: 'en-CA',
  },
  components: {
    VDateInput,
  },
  theme: {
    themes: {
      dark: {
        colors: {
          primary: colors.purple.darken1,
        }
      },
    },
    defaultTheme: 'dark',
  },
})