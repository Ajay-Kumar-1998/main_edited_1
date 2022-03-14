const add_deck = Vue.component("add_deck", {
  props: ["user"],
  data: function () {
    return {
      new_deck_name: "",
    };
  },
  template: `
 
    <form id="add_deck" action="/api/deck/{{user}}" method="POST">
    <label for="deck_name" class="form-label">Deck name</label>
    <input type="text" name="deck_name" class="form-control"  placeholder="Enter Deck Name" v-model="new_deck_name"/>
    <button type="submit" id="deck_add_btn" class="btn btn-outline-secondary" v-on:click="add_deck_func" >
     ADD
    </button>
    </form>
    
    `,
  methods: {
    add_deck: function (deck_name) {},
  },
});

var app = new Vue({
  el: "#app",
});

console.log("in js file===============================");
