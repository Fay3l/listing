<script setup lang="ts">
import { jsPDF } from "jspdf";
import autoTable from 'jspdf-autotable'
import { type Product } from "./../product.ts";
import { useI18n } from "vue-i18n";
const { t } = useI18n();
defineProps<{
    items: Product[];
    total: number;
    isEmpty: boolean;
}>();
function downloadPDF(products: Product[], total: number) {
    const doc = new jsPDF();
    doc.setFontSize(18);
    doc.text('MyLyst', 14, 22);
    doc.setFontSize(12);
    doc.text(t('slogan'), 14, 36);
    autoTable(doc, {
        startY: 42, 
        head: [[t('card.person'), t('card.place'), t('card.product'), t('card.price')]],
        body: products.map(item => [
            item.person,
            item.place,
            item.product,
            `${item.price.toFixed(2)} ${t('currency')}`
        ]),
    })

    const finalY = (doc as any).lastAutoTable.finalY
    doc.setFontSize(14)
    doc.text(`${t('total')} : ${total.toFixed(2)} ${t('currency')}`, 14, finalY + 10)

    doc.save('mylyst.pdf')


}
</script>

<template>
    <button class="border-1 text-black p-2 rounded-md hover:bg-gray-200" @click="downloadPDF(items, total)"
        :disabled="isEmpty">
        <div class="flex items-center justify-center">
            <img src="/icons/pdf.svg" alt="Download" class="w-5 h-5 mr-2" />
            {{ $t('downloadpdf') }}
        </div>
    </button>
</template>