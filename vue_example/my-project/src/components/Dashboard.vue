<template>
 <div class='dashboard'>
   <nav>
   </nav>

   <div class='left'>
    <Card
      header='Flights'
    />
   </div>

   <div class='center'>
    <Card 
      header='Map'
    />
   </div>

   <div class='right'>
    <Card 
      header='Table'
    />
   </div>
 </div>
</template>

<script>
import Card from './Card';

export default {
  name: 'Dashboard',
  components: {
    Card,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.dashboard {
  width: 100%;
  height: 100%;

  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 100px auto;
}

.dashboard > nav {
  grid-column: 1 / 4;
  grid-row: 1 / 2;
  background-color: rgba(0, 0, 0, 0.8);
}

.dashboard > div {
  grid-row: 2 / 3;
  background-color: rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.dashboard > .left {
  grid-column: 1 / 2;
}

.dashboard > .center {
  grid-column: 2 / 3;
}

.dashboard > .right {
  grid-column: 3 / 4;
}
</style>
