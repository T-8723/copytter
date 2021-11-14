import { Options, Vue } from "vue-class-component";
import { ElForm } from "element-plus";

import { AuthApi } from "@/common/services/openapi";
import { FormRulesMap } from "element-plus/es/components/form/src/form.type";
import { InternalRuleItem } from "async-validator";

@Options({})
export default class Auth extends Vue {
  /** 子コンポーネントのテンプレートを参照するための定義を追加 */
  declare $refs: {
    refForm: InstanceType<typeof ElForm>;
  };

  API_auth = new AuthApi(undefined, process.env.VUE_APP_API_BASE_URL);
  auth_check = true;

  form: {
    username: string;
    pass: string;
    checkPass: string;
  } = {
    username: "",
    pass: "",
    checkPass: "",
  };

  rules: FormRulesMap = {
    pass: [
      {
        required: true,
        trigger: "change",
        message: "必須項目です",
      },
      {
        validator: (
          _rule: InternalRuleItem,
          value: string,
          callback: (error?: string | Error | undefined) => void
        ): void => {
          if (value.length < 8) {
            callback(new Error("8文字以上で入力してください"));
          } else {
            callback();
          }
        },
        trigger: "change",
      },
    ],
    checkPass: [
      {
        required: true,
        trigger: "change",
        message: "必須項目です",
      },
      {
        validator: (
          _rule: InternalRuleItem,
          value: string,
          callback: (error?: string | Error | undefined) => void
        ): void => {
          if (value.length < 8) {
            callback(new Error("8文字以上で入力してください"));
          } else if (value !== this.form.pass) {
            callback(new Error("パスワードが一致しません"));
          } else {
            callback();
          }
        },
        trigger: "change",
      },
    ],
  };

  data(): {
    form: {
      username: string;
      pass: string;
      checkPass: string;
    };

    rules: FormRulesMap;
  } {
    return {
      form: this.form,
      rules: this.rules,
    };
  }

  login(): void {
    this.$refs.refForm.validate()?.then((valid) => {
      if (valid) {
        this.auth_check = true;
        this.API_auth.authCreate({
          username: this.form.username,
          password: this.form.pass,
        })
          .then((response) => {
            /** なぜか openapi-generator-cli で生成したレスポンス型のここだけ実態と違う */
            const responseData = response.data as unknown as { token: string };
            this.$store.dispatch("auth/setUserInfo", responseData.token);

            this.$router.push("Home");
          })
          .catch(() => {
            this.auth_check = false;
          });
      }
    });
  }

  cancel(): void {
    this.$router.push("Home");
  }
}
