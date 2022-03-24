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
                <div class="col-md-7" id="deck_name_div">
                  <p id="deck_name" >{{deck ['deck_name']}}</p>
                </div>

                <div class="col-md-1" id="deck_features_s">
                  <p>{{deck['score']}}</p>
                </div>
                <div class="col-md-1" id="deck_features">
                  <router-link to="/review/{{ deck['deck_name'] }}"><i class="bi bi-arrow-right-circle"></i></router-link>
                </div>
                <div class="col-md-1" id="deck_features">
                  <i class="bi bi-pencil-square fa-5x"></i>
                </div>
                <div class="col-md-1" id="deck_features">
                  <i class="bi bi-download"></i>
                </div>
                <div class="col-md-1" id="deck_features" v-on:click="delete_deck(deck['deck_name'])" >
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

    delete_deck: function (deck_name) {
      fetch(`/ajay kumar3/deck/${deck_name}/delete`, {
        method: "GET",
      })
        .then((resp) => resp.json())
        .then(() => console.log("deleted deck--------------"))
        .catch((e) => console.log(e));
    },

    edit_deck_form: function () {
      Document.getElementById("deck_name").innerHTML =
        "<form><input type='text' class='form-control' placeholder='new name'><button class='btn btn-success'></form>";
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

// ==============================  review deck  ============================
const review = Vue.component("review", {
  data: function () {
    return {
      user: null,
    };
  },
  template: `
  <div class="row">
  <div class="col-md-2"></div>
  <div class="col-md-2" id="review_deck_info"></div>
  <div class="col-md-4" id="main_card"></div>
  <div class="col-md-2" id="review_buttons">
    <div class="row" id="btn-1"></div>
    <div class="row" id="btn-2"></div>
    <div class="row" id="btn-3"></div>
  </div>
  <div class="col-md-2"></div>
  <h1>{{ $route.params.deck }}</h1>
  </div>
  `,
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
  { path: "/review/:deck", component: review },
];
const router = new VueRouter({
  routes, // short for `routes: routes`
});

var app = new Vue({
  el: "#app",
  delimiters: ["{%", "%}"],
  router: router,
});

console.log("in js file =============================== ");
