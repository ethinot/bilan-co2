<template>
  <div v-if="$parent.isOpen">
    <slot />
  </div>
</template>