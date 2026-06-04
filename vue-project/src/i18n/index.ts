import { createI18n } from 'vue-i18n'
import fr from './locales/fr.json'
import en from './locales/en.json'
import es from './locales/es.json'
import de from './locales/de.json'
import enUS from './locales/enUS.json'

export const i18n = createI18n({
    locale: 'fr',
    messages: { fr, en, es, de, "en-US": enUS }
})

