<template>
    <div class="card">
      <header>
      </header>

      <content>
      </content>

      <footer>
      </footer>
    </div>
</template>

<script>
export default {
  name: 'Card',
  props: {
    header: String,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
div.card {
  width: 100%;
  height: 100%;

  display: grid;

  grid-template-rows: 75px auto 75px;
  grid-template-columns: auto;
}

.card > header {
  background-color: rgba(0,0,0,0.5);
}

.card > footer {
  background-color: rgba(0,0,0,0.5);
}
</style>
