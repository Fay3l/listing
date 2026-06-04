<script setup lang="ts">
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";
import { v4 as uuidv4 } from "uuid";
const langues = [
  { code: "fr", label: "Français", icon: "/icons/flag-france.svg" },
  { code: "en", label: "English", icon: "/icons/flag-us.svg" },
  { code: "es", label: "Español", icon: "/icons/flag-es.svg" },
  { code: "de", label: "Deutsch", icon: "/icons/flag-de.svg" }
]
const { locale } = useI18n()
const langueActive = computed(() => langues.find(l => l.code === locale.value))
type Product = {
  id: string;
  personne: string;
  lieu: string;
  produit: string;
  prix: number;
};
const isEditing = ref(false);
const id = ref(uuidv4());
const personne = ref("");
const lieu = ref("");
const produit = ref("");
const prix = ref(0);
const items = ref<Product[]>([]);
let total = ref(0);
function ajouterProduit(item: Product) {
  items.value.push(item);
  total.value += item.prix;
  produit.value = "";

}
function validerModification(item: Product) {
  const index = items.value.findIndex((p) => p.id === item.id);
  const oldPrice = items.value[index]?.prix || 0;
  if (index !== -1) {
    total.value -= oldPrice; // Soustraire l'ancien prix
    total.value += item.prix; // Ajouter le nouveau prix
    items.value[index] = { ...item }; // Mettre à jour le produit
    isEditing.value = false;
    personne.value = "";
    lieu.value = "";
    produit.value = "";
    prix.value = 0;
  }
}

async function changerLangue(lang: string) {
  locale.value = lang;
}

</script>

<template>
  <div class="flex flex-row items-center justify-between  m-8">
    <div>
      <p class="text-2xl font-bold">MyLyst</p>
    </div>
    <div class="flex flex-row items-center gap-2">
      <div>
        <img :src="langueActive?.icon" :alt="langueActive?.label" class="w-8 h-8" />
      </div>
      <select v-model="locale" class="border border-gray-300 rounded-md p-2">
        <option v-for="lang in langues" :key="lang.code" :value="lang.code">
          {{ lang.label }}
        </option>
      </select>
    </div>
  </div>


  <div class="flex gap-4 flex-row justify-center items-center max-lg:grid grid-cols-2 m-3">
    <input type="text" class="border border-black rounded-md p-2" v-model="personne"
      :placeholder="$t('placeholder.person')" />
    <input type="text" class="border border-black rounded-md p-2" v-model="lieu"
      :placeholder="$t('placeholder.place')" />
    <input type="text" class="border border-black rounded-md p-2" v-model="produit"
      :placeholder="$t('placeholder.product')" />
    <input type="number" class="border border-black rounded-md p-2" v-model="prix"
      :placeholder="$t('placeholder.price')" step="0.01" />
    <button class="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 max-lg:col-span-2" @click="
      isEditing
        ? validerModification({
          id: id,
          personne: personne,
          lieu: lieu,
          produit: produit,
          prix: prix,
        })
        : ajouterProduit({
          id: id,
          personne: personne,
          lieu: lieu,
          produit: produit,
          prix: prix,
        })
      ">
      {{ isEditing ? $t('button.edit') : $t('button.add') }}
    </button>
    <button id="modifierBtn" style="display: none" onclick="validerModification()"
      class="bg-green-500 text-white p-2 rounded-md hover:bg-green-600">
      {{ $t('button.validate') }}
    </button>
  </div>

  <div class="flex justify-center items-center m-3" v-for="item in items" :key="item.id">
    <div class="flex justify-between items-center border border-gray-300 rounded-md p-4 w-full max-w-md">
      <div>
        <p>Personne: {{ item.personne }}</p>
        <p>Lieu: {{ item.lieu }}</p>
        <p>Produit: {{ item.produit }}</p>
        <p>Prix: {{ item.prix.toFixed(2) }} {{ $t('currency') }}</p>
      </div>
      <div class="flex flex-col">
        <button class="bg-yellow-500 text-white p-2 rounded-md hover:bg-yellow-600 m-2" @click="
          (id = item.id),
          (personne = item.personne),
          (lieu = item.lieu),
          (produit = item.produit),
          (prix = item.prix);
        isEditing = true;
        ">
          {{ $t('button.edit') }}
        </button>
        <button class="bg-red-500 text-white p-2 rounded-md hover:bg-red-600 m-2" @click="">
          {{ $t('button.remove') }}
        </button>
      </div>
    </div>
  </div>

  <div class="flex justify-center m-10">Total: {{ total.toFixed(2) }} {{ $t('currency') }}</div>
</template>

<style scoped></style>
