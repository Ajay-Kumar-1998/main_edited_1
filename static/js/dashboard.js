const add_deck = Vue.component("add_deck", {
  props: ["user"],
  template: `
  <div>
    <form id="add_deck" action="/api/deck/{{user}}" method="POST">
    <label for="deck_name" class="form-label">Deck name</label>
    <input type="text" name="deck_name" class="form-control"  placeholder="Enter Deck Name" v-model="new_deck_name"/>
    <button type="submit" id="deck_add_btn" class="btn btn-outline-secondary" v-on:click="add_deck_func" >
     ADD
    </button>
    </form>
    </div>`,
  data: function () {
    return {
      new_deck_name: null,
    };
  },
  methods: {
    add_deck_func: function () {},
  },
});

var features = new Vue({
  el: "#app",
});
