import { Options, Vue } from "vue-class-component";
import { ElForm } from "element-plus";

import { AuthInfo } from "@/common/types/common";
import { ApiApi, SelfProfile } from "@/common/services/openapi";
import { FormRulesMap } from "element-plus/es/components/form/src/form.type";

@Options({})
export default class Profile extends Vue {
  /** 子コンポーネントのテンプレートを参照するための定義を追加 */
  declare $refs: {
    refForm: InstanceType<typeof ElForm>;
  };

  API = new ApiApi(undefined, process.env.VUE_APP_API_BASE_URL);
  auth_check = true;

  form: SelfProfile = {
    id: 0,
    gender: undefined,
    birth_date: undefined,
    location: undefined,
    age: undefined,
    icon_pass: undefined,
    profile_message: undefined,
    status: undefined,
    profile_user_id: undefined,
    sensitive_entry: undefined,
    profile_first_registed: false,
    user: 0,
  };

  rules: FormRulesMap = {};

  mounted(): void {
    this.checkLoginUser();
  }

  data(): {
    form: SelfProfile;
    rules: FormRulesMap;
  } {
    return {
      form: this.form,
      rules: this.rules,
    };
  }

  private checkLoginUser() {
    const authInfo: AuthInfo = this.$store.getters["auth/getUserInfo"];
    const token: string | undefined = this.$store.getters["auth/getToken"];
    const user: SelfProfile = this.$store.getters["user/getUser"];

    if (!authInfo.user_id || token === "") {
      this.$router.push("Home");
    } else {
      this.form = user;
    }
  }

  registProfile(): void {
    this.$router.push("");
  }
}
