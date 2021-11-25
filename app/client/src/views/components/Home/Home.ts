import { Options, Vue } from "vue-class-component";

import Entry from "@/common/components/Entry/Entry.vue";
import Main from "@/common/components/Main/Main.vue";
import { ApiApi, Entry as Entries } from "@/common/services/openapi";

@Options({
  components: { Entry, Main },
})
export default class Home extends Vue {
  API = new ApiApi(undefined, process.env.VUE_APP_API_BASE_URL);
  entries: Entries[] = [];

  mounted(): void {
    this.requestEntriesList();
  }

  requestEntriesList(): void {
    this.API.apiEntriesList()
      .then((response) => {
        console.log(response);
        const entries = response.data;
        if (entries.length > 0) {
          this.entries = entries;
          entries.forEach((item) => {
            this.getProfile(item.author.id);
          });
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }

  getProfile(id: number): void {
    this.API.apiProfileRetrieve(id)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }
}
