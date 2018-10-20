<template>
  <div id="app">
    <b-table
      class="left"
      hover
      :items="flights"
      @row-clicked="flightTableClick"
    />
    <b-table
      class="right"
      hover
      :items="objects"
      @row-clicked="objectsTableClick"
    />
  </div>
</template>

<script>

function flightTableClick(record, index) {
  if (this.selectedFlights.includes(record.id)) {
    this.selectedFlights = this.selectedFlights.filter(x => x != record.id);
  } else {
    this.selectedFlights.push(record.id);
  }
  this.objects = [];
  for (let i of this.selectedFlights)
  {
    fetch(`http://localhost:8000/flight/${i}/objects`)
      .then(response => response.json())
      .then(
        json => {
          this.objects = this.objects.concat(json);
        }
      );
  }
}

function objectsTableClick(record, index) {
  // nothing
}

function created() {
  fetch("http://localhost:8000/flight")
  .then(response => response.json())
  .then(
    json => {
      this.flights = json;
    }
  );
}

export default {
  name: 'app',
  methods: {
    flightTableClick,
    objectsTableClick,
  },
  data () {
    return {
      objects: [],
      flights: [],
      selectedFlights: [],
    }
  },
  created,
}

</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

  display: grid;
  grid-template-columns: 50px 1fr 50px 3fr 50px;
  grid-template-rows: auto;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.left {
  grid-column-start: 2;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 2;
}

.right {
  grid-column-start: 4;
  grid-column-end: 5;
  grid-row-start: 1;
  grid-row-end: 2;
}

</style>
