// ============================== YOUR DECKS ============================
const your_decks = Vue.component("your_decks", {
  data: function () {
    return {
      user: null,
    };
  },
  template: `
  <h1>sample your deck component</h1>`,
});

// =================================== ADD DECK ===============

const add_deck = Vue.component("add_deck", {
  props: ["user"],
  data: function () {
    return {
      deck_name: null,
      btn_class: null,
    };
  },
  template: `
 
    <form id="add_deck" @submit.prevent="add_deck_func">
    <label for="deck_name" class="form-label">Deck name</label>
    <input type="text" name="deck_name" class="form-control"  placeholder="Enter Deck Name" v-model="deck_name"/>
    <button id="deck_add_btn" class="btn btn-outline-secondary"  v-bind:class="btn_class" >
     ADD
    </button>
    </form>
    
    `,
  methods: {
    add_deck_func: function () {
      this.btn_class = "btn btn-warning";
      fetch(`/api/deck/${this.user}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ deck_name: this.deck_name }),
      })
        .then((resp) => resp.json())
        .then(() => (this.btn_class = "btn btn-outline-success"))
        .catch((e) => console.log(e));
    },
  },
});

// ============================== ROUTES ====================
routes_ = [{ path: "/", component: your_decks }];
const router = new VueRouter({
  routes_, // short for `routes: routes`
});

var app = new Vue({
  el: "#app",
  router: router,
});

console.log("in js file===============================");
