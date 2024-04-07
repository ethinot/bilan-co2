<template>
  <div>
      <Menu class="relative inline-block text-left py-5 px-10 " >
         <MenuButton 
         class="w-full flex justify-center gap-x-1.5 text-zinc-50 rounded-xl bg-[#03C988] px-2 py-2 text-lg font-semibold shadow-sm ring-1 ring-inset ring-gray-300 h-14" id="menu-button" aria-expanded="true" aria-haspopup="true">
         Ajouter un traqueur <img src="./ajout.png" class="h-7" alt="">
         </MenuButton>
         <MenuItems class="absolute right-0 z-10 mt-2 w-18 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1" >
            <div class="py-1" role="none">
            <MenuItem class="text-gray-700 block px-4 py-2 text-sm" > <img src="./MenuImage/car_23773.png" class="h-9" alt=""> </MenuItem>
            <MenuItem class="text-gray-700 block px-4 py-2 text-sm"><img src="./MenuImage/food.png" class="h-9" alt=""></MenuItem>
            </div>
         </MenuItems>
      </Menu>
  </div>
</template>
<script>
import Menu from './Menu.vue';
import MenuButton from './MenuButton.vue';
import MenuItems from './MenuItems.vue';
import MenuItem from './MenuItem.vue';

export default {
    components: {
        Menu,
        MenuButton,
        MenuItems,
        MenuItem
    }
}

</script>