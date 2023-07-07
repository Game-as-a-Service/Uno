import { APP_INITIALIZER } from "@angular/core";
import { ConfigService } from "./config.service";

function initConfigService(config: ConfigService): any {
  return () => config.load();
}

// ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

export const ConfigServiceLoader = {
  provide: APP_INITIALIZER,
  useFactory: initConfigService,
  deps: [ConfigService],
  multi: true,
};
