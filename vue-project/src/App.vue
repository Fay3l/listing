<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { useI18n } from "vue-i18n";
import { v4 as uuidv4 } from "uuid";
import { type Product } from "./product.ts";
import DocumentPdf from "./components/DocumentPdf.vue";
import MessagePopUp from "./components/MessagePopUp.vue";
import { addProductInDB, deleteProductInDB, getProductsInDB, getTotalProductsInDB, openDB, updateProductInDB } from "./IndexedDB/db.ts";
const langues = [
  { code: "fr", label: "Français", icon: "/icons/flag-fr.svg" },
  { code: "en", label: "English", icon: "/icons/flag-gb.svg" },
  { code: "es", label: "Español", icon: "/icons/flag-es.svg" },
  { code: "de", label: "Deutsch", icon: "/icons/flag-de.svg" },
  { code: "en-US", label: "English (US)", icon: "/icons/flag-us.svg" },
]
const { locale, t } = useI18n()
onMounted(async () => {
  await openDB()
  items.value = await getProductsInDB()
  total.value = await getTotalProductsInDB()
})
const langueActive = computed(() => langues.find(l => l.code === locale.value))
const isEmpty = computed(() => items.value.length === 0);
const isEditing = ref(false);
const Message = ref({
  message: "",
  type: "",
  disabled: true,
})
const showMessage = (message: string, type: string) => {
  Message.value = { message, type, disabled: false };
  setTimeout(() => {
    Message.value.disabled = true;
  }, 2000);
}
const id = ref(uuidv4());
const personne = ref("");
const lieu = ref("");
const produit = ref("");
const prix = ref(0);
const items = ref<Product[]>([]);
let total = ref(0);
async function ajouterProduit(item: Product) {
  if (!item.person || !item.place || !item.product) {
    showMessage(t('message.error'), "Error");
    return;
  }
  await addProductInDB(item)
  items.value = await getProductsInDB()
  total.value = await getTotalProductsInDB()
  showMessage(t('message.success'), "Success");
  produit.value = "";

}
async function validerModification(item: Product) {
  await updateProductInDB(item)
  items.value = await getProductsInDB()
  total.value = await getTotalProductsInDB()
  isEditing.value = false;
  showMessage(t('message.edit'), "Success"); 
  produit.value = "";
  prix.value = 0;
}

async function supprimerProduit(id: string) {
  isEditing.value = false;
  await deleteProductInDB(id)
  items.value = await getProductsInDB()
  total.value = await getTotalProductsInDB()
  showMessage(t('message.remove'), "Success");

}

</script>

<template>
  <MessagePopUp :message="Message.message" :type="Message.type" :disabled="Message.disabled" />
  <div class="flex flex-row items-center justify-between  m-8">
    <div>
      <p class="text-2xl font-bold">MyLyst</p>
    </div>
    <div class="flex flex-row items-center gap-2">
      <div>
        <img :src="langueActive?.icon" :alt="langueActive?.code" class="w-8 h-8" />
      </div>
      <select v-model="locale" class="border border-gray-300 rounded-md p-2">
        <option v-for="lang in langues" :key="lang.code" :value="lang.code">
          {{ lang.label }}
        </option>
      </select>
    </div>
  </div>

  <div class="flex flex-col items-center justify-center m-5">
    <h1 class="text-lg font-bold mb-2">{{ $t('slogan', 2) }}</h1>
  </div>


  <div class="grid grid-cols-2 items-center gap-4  justify-center m-8 ">
    <input type="text" class="border border-black rounded-md p-2" v-model="personne"
      :placeholder="$t('placeholder.person')" />
    <input type="text" class="border border-black rounded-md p-2" v-model="lieu"
      :placeholder="$t('placeholder.place')" />
    <input type="text" class="border border-black rounded-md p-2" v-model="produit"
      :placeholder="$t('placeholder.product')" />
    <input type="number" class="border border-black rounded-md p-2" v-model="prix"
      :placeholder="$t('placeholder.price')" step="0.01" min="0" />
    <div class="grid col-span-2 items-center justify-stretch">
      <DocumentPdf :items="items" :isEmpty="isEmpty" :total="total" />
    </div>
    <button class="col-span-2 bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 " @click="
      isEditing
        ? validerModification({
          id: id,
          person: personne,
          place: lieu,
          product: produit,
          price: prix,
          isChecked:false
        })
        : ajouterProduit({
          id: uuidv4(),
          person: personne,
          place: lieu,
          product: produit,
          price: prix,
          isChecked:false
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
        <p>{{ $t('card.person') }}: {{ item.person }}</p>
        <p>{{ $t('card.place') }}: {{ item.place }}</p>
        <p>{{ $t('card.product') }}: {{ item.product }}</p>
        <p>{{ $t('card.price') }}: {{ item.price.toFixed(2) }} {{ $t('currency') }}</p>
      </div>
      <div class="flex flex-col">
        <button class="bg-yellow-500 text-white p-2 rounded-md hover:bg-yellow-600 m-2" @click="
          (id = item.id),
          (personne = item.person),
          (lieu = item.place),
          (produit = item.product),
          (prix = item.price);
        isEditing = true;
        ">
          {{ $t('button.edit') }}
        </button>
        <button class="bg-red-500 text-white p-2 rounded-md hover:bg-red-600 m-2" @click="supprimerProduit(item.id)">
          {{ $t('button.remove') }}
        </button>
      </div>
    </div>
  </div>

  <div class="flex justify-center m-10">Total: {{ total.toFixed(2) }} {{ $t('currency') }}</div>
</template>

<style scoped></style>
