import { Options, Vue } from "vue-class-component";

import { ApiApi, EntryStatusEnum, SelfProfile } from "@/common/services/openapi";
import { AuthInfo } from "@/common/types/common";
import { More, Location, Document, Menu as IconMenu, Setting } from "@element-plus/icons";
import { ElMessage } from "element-plus";

@Options({
  components: { More, Location, Document, IconMenu, Setting },
})
export default class Main extends Vue {
  API = new ApiApi(undefined, process.env.VUE_APP_API_BASE_URL);

  profile!: SelfProfile;
  isCollapse = true;
  textarea = "";

  circleUrl = "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png";

  get visibleOnlyLoginedUser(): boolean {
    return this.profile?.profile_user_id ? false : true;
  }

  data(): {
    textarea: string;
    profile: SelfProfile;
    circleUrl: string;
  } {
    return {
      textarea: this.textarea,
      profile: this.profile,
      circleUrl: this.circleUrl,
    };
  }

  mounted(): void {
    this.checkLoginUser();
  }

  private checkLoginUser() {
    const authInfo: AuthInfo = this.$store.getters["auth/getUserInfo"];
    const token: string | undefined = this.$store.getters["auth/getToken"];

    if (authInfo.user_id && token !== "") {
      this.API.apiSelfprofileRetrieve(authInfo.user_id, {
        headers: {
          Authorization: `JWT ${token}`,
        },
      }).then((response) => {
        this.profile = response.data;
        this.$store.dispatch("profile/setProfile", this.profile);

        if (!response.data.profile_first_registed) {
          this.$router.push("Profile");
        }
      });
    }
  }

  toAuth(): void {
    this.$router.push("Auth");
  }

  sendEntry(): void {
    const token: string | undefined = this.$store.getters["auth/getToken"];
    this.API.apiCreateEntryCreate(
      {
        id: NaN,
        author: this.profile,
        body: this.textarea,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      },
      {
        headers: {
          Authorization: `JWT ${token}`,
        },
      }
    ).then(() => {
      ElMessage.info({
        message: "投稿しました。",
      });
    });
  }
}
