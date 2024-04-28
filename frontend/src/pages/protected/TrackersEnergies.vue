<script setup>
import Save from '@/components/save/Save.vue';
</script>

<template>
 
 <div class="relative ">
  <div class="absolute left-1/2 z-10 mt-5 flex w-screen max-w-max -translate-x-1/2 px-4">
    <div class="w-screen max-w-5xl flex-auto overflow-hidden rounded-3xl bg-white text-sm leading-6 shadow-lg ring-1 ring-gray-900/5">
      <div class="p-4 grid grid-cols-2">
        <div class="group relative flex gap-x-6 rounded-lg p-4 hover:bg-gray-100" v-for="(subCategories, category) in categories" :key="category"  >
          <div class="mt-1 flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
          </div>
          <div >
            <a href="#" class="font-semibold text-gray-900">
              {{ category }}
              <span class="absolute inset-0"></span>
            </a>
            <p class="mt-1 text-gray-600"></p><b/>
          </div>
        </div>
      </div>
      <Save/>
    </div>
  </div>
</div>


</template>
<script>
export default {
  data() {
    return {
      categories: {
                    "aides culinaires et ingrédients divers": ["aides culinaires", "sauces", "sels", "condiments", "denrées destinées à une alimentation particulière", "herbes", "algues", "ingrédients divers", "épices"],
                    "aliments infantiles": ["desserts infantiles", "petits pots salés et plats infantiles", "céréales et biscuits infantiles", "laits et boissons infantiles"],
                    "boissons": ["boissons sans alcool", "boisson alcoolisées", "eaux"],
                    "entrées et plats composés": ["feuilletées et autres entrées", "sandwichs", "pizzas, tartes et crêpes salées", "soupes", "salades composées et crudités", "plats composés", "plats végétariens"],
                    "fruits, légumes, légumineuses et oléagineux": ["fruits à coque et graines oléagineuses", "légumes", "pommes de terre et autres tubercules", "légumineuses", "fruits"],
                    "glaces et sorbets": ["sorbets", "glaces", "desserts glacés"],
                    "lait et produits laitiers": ["crèmes et spécialités à base de crème", "fromages", "laits", "produits laitiers frais et assimilés"],
                    "matières grasses": ["autres matières grasses", "margarines", "huiles de poissons", "beurres", "huiles et graisses végétales"],
                    "produits céréaliers": ["gâteaux et pâtisseries", "céréales de petit-déjeuner et biscuits", "pâtes, riz et céréales", "pains et viennoiseries", "farines et pâtes à tarte"],
                    "produits sucrés": ["sucres, miels et assimilés", "confitures et assimilés", "chocolats et produits à base de chocolat", "confiseries non chocolatées"],
                    "viandes, œufs, poissons": ["poissons cuits", "autres produits à base de viande", "substituts de charcuterie", "viandes cuites", "substituts de viande", "charcuteries", "mollusques et crustacés cuits", "œufs", "viandes crues", "poissons crus", "produits à base de poissons et produits de la mer", "mollusques et crustacés crus"]
                }
    }
  },
}

</script>