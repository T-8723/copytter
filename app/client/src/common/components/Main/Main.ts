import { Options, Vue } from "vue-class-component";

import { ApiApi, SelfProfile } from "@/common/services/openapi";
import { AuthInfo } from "@/common/types/common";
import { Location, Document, Menu as IconMenu, Setting } from "@element-plus/icons";

@Options({
  components: { Location, Document, IconMenu, Setting },
})
export default class Main extends Vue {
  API = new ApiApi(undefined, process.env.VUE_APP_API_BASE_URL);

  user!: SelfProfile;
  isCollapse = true;

  get visibleLoginButton(): boolean {
    return this.user?.profile_user_id ? false : true;
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
        this.user = response.data;
        this.$store.dispatch("user/setUser", this.user);

        if (!response.data.profile_first_registed) {
          this.$router.push("Profile");
        }
      });
    }
  }

  toAuth(): void {
    this.$router.push("Auth");
  }
}
