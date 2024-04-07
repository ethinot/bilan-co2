<template>
  <button @click="$parent.toogle()" class="border">
    <slot />
  </button>
</template>