const add_deck = Vue.component("add_deck", {
  props: ["test"],
  template: `
  <form>
  <input type="text">
  <button>Add deck</button>
</form>
    `,
});

const delete_deck = Vue.component("delete_deck", {
  props: ["test"],
  template: `
  <form>
  <input type="text">
  <button>delete deck</button>
</form>
  `,
});

const routes = [
  {
    path: "/",
    component: add_deck,
  },
  {
    path: "/delete_deck",
    component: delete_deck,
  },
];

const router = new VueRouter({
  routes, // short for `routes: routes`
});

var app = new Vue({
  el: "#app",
  router: router,
});

console.log("in testing js");
