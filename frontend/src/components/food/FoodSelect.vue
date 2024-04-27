<template>
    <div>
     <h1> Calculer le bilan de vos aliments</h1>
     <div v-for="food in foods" class="grid grid-rows-1 grid-flow-col gap-4 p-6">
     <div class=" bg-green-200 " @clik="selectFoods">{{ name }}</div>
     </div>
      <div v-if="selectFoods.length ">

      </div>  
    </div>
</template>
<script>
import axios from 'axios'

// export default {
//     data() {
//         return {
//             foods: [],
//             selectFoods: []
//         },
//         methods: {
//             axios()
//             .get('baseurl')
//             .then(response => {
//                 this.foods = response.data
//             })
//             .catch(error => console.log(error)),
            
//             selectFoods(food) {
//                 this.selectFoods.push(food)}
//         }
        
//     }
// }

</script>