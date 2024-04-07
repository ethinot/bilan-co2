<template>
  <div>
    <slot :is-open="isOpen" />
  </div>
</template>
<script> 
  export default {
    data() {
        return {
            isOpen: false,
        }
    },
    methods: {
        Open() {
            this.isOpen = true;
        },
        Close() {
            this.isOpen = false;
        },
        toogle() {
            this.isOpen = !this.isOpen;
        }
    },
  }
</script>