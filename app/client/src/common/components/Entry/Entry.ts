import { Options, Vue } from "vue-class-component";
import { PropType } from "vue";
import { ApiApi, Profile, User, Entry as EntryType } from "@/common/services/openapi/api";

import { More, RefreshLeft, Star } from "@element-plus/icons";
@Options({
  props: {
    entry: {
      type: Object as PropType<EntryType>,
      require: true,
    },
  },
  components: { More, RefreshLeft, Star },
})
export default class Entry extends Vue {
  API = new ApiApi(undefined, process.env.VUE_APP_API_BASE_URL);

  entry!: EntryType;
  profile!: Profile;
  user!: User;
  circleUrl = "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png";

  data(): {
    profile: Profile;
    user: User;
  } {
    return {
      profile: this.profile,
      user: this.user,
    };
  }

  mounted(): void {
    this.user = this.entry.author;
    this.getProfile(this.entry.author.id);
  }

  async getProfile(id: number): Promise<void> {
    this.profile = (await this.API.apiProfileRetrieve(id)).data;
  }
}
