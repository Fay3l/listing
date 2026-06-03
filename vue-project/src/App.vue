<script setup lang="ts">
import { ref } from "vue";
type Product = {
  id: number;
  personne: string;
  lieu: string;
  produit: string;
  prix: number;
};
const isEditing = ref(false);
const id = ref(Date.now());
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
  const oldPrice = items.value[index]?.prix || 0 ;
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
</script>

<template>
  <div class="flex justify-center m-4">
    <p class="text-lg font-bold">MyLyst</p>
  </div>

  <div class="flex gap-4 flex-row justify-center items-center max-lg:grid grid-cols-2 m-3">
    <input
      type="text"
      class="border border-black rounded-md p-2"
      v-model="personne"
      placeholder="Nom de la personne"
    />
    <input
      type="text"
      class="border border-black rounded-md p-2"
      v-model="lieu"
      placeholder="Lieu d'achat"
    />
    <input
      type="text"
      class="border border-black rounded-md p-2"
      v-model="produit"
      placeholder="Nom du produit"
    />
    <input
      type="number"
      class="border border-black rounded-md p-2"
      v-model="prix"
      placeholder="Prix (€)"
      step="0.01"
    />
    <button
      class="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 max-lg:col-span-2"
      @click="
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
      "
    >
      {{ isEditing ? "Modifier" : "Ajouter" }}
    </button>
    <button
      id="modifierBtn"
      style="display: none"
      onclick="validerModification()"
      class="bg-green-500 text-white p-2 rounded-md hover:bg-green-600"
    >
      Valider la modification
    </button>
  </div>

  <div class="flex justify-center items-center m-3" v-for="item in items" :key="item.id">
    <div
      class="flex justify-between items-center border border-gray-300 rounded-md p-4 w-full max-w-md"
    >
      <div>
        <p>Personne: {{ item.personne }}</p>
        <p>Lieu: {{ item.lieu }}</p>
        <p>Produit: {{ item.produit }}</p>
        <p>Prix: {{ item.prix.toFixed(2) }} €</p>
      </div>
      <div class="flex flex-col">
        <button
          class="bg-yellow-500 text-white p-2 rounded-md hover:bg-yellow-600 m-2"
          @click="
            (id = item.id),
            (personne = item.personne),
              (lieu = item.lieu),
              (produit = item.produit),
              (prix = item.prix);
            isEditing = true;
          "
        >
          Modifier
        </button>
        <button
          class="bg-red-500 text-white p-2 rounded-md hover:bg-red-600 m-2"
          @click=""
        >
          Supprimer
        </button>
      </div>
    </div>
  </div>

  <div class="flex justify-center m-10">Total: {{ total.toFixed(2) }} €</div>
</template>

<style scoped></style>
