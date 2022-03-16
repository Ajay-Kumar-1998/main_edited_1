// ============================== YOUR DECKS ============================
const your_decks = Vue.component("your_decks", {
  data: function () {
    return {
      deck_list: [],
    };
  },
  template: `
  <div>
 
  <div class="container" id="main_deck_cont" v-for="deck in deck_list">
              <div class="row">
                <div class="col-md-7">
                  <p>{{deck ['deck_name']}}</p>
                </div>

                <div class="col-md-1" id="deck_features_s">
                  <p>{{deck['score']}}</p>
                </div>
                <div class="col-md-1" id="deck_features">
                  <i class="bi bi-arrow-right-circle"></i>
                </div>
                <div class="col-md-1" id="deck_features">
                  <i class="bi bi-pencil-square fa-5x"></i>
                </div>
                <div class="col-md-1" id="deck_features">
                  <i class="bi bi-download"></i>
                </div>
                <div class="col-md-1" id="deck_features" >
                  <i class="bi bi-trash"></i>
                </div>
              </div>
            </div> 
  </div>`,

  methods: {
    get_deck_list: function () {
      fetch(`/api/deck/ajay kumar3`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((deck_info) => deck_info.json())
        .then((deck_info) => this.deck_list.push(...deck_info))
        .catch((e) => console.log(e));
    },
  },

  mounted: function () {
    this.get_deck_list();
  },
});

// ==============================  analatics ============================
const analatics = Vue.component("analatics", {
  data: function () {
    return {
      user: null,
    };
  },
  template: `
  <h1>sample Analatics component</h1>`,
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
routes = [
  { path: "/", component: your_decks },
  { path: "/analatics", component: analatics },
];
const router = new VueRouter({
  routes, // short for `routes: routes`
});

var app = new Vue({
  el: "#app",
  router: router,
});

console.log("in js file===============================");
