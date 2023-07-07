import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { ConfigSetting, devConfigSetting } from './config.schema';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {

  static useSetting: ConfigSetting;

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  constructor(
    private http: HttpClient,
  ) { }

  // ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

  async load(): Promise<void> {

    if (environment.production === true) {
      const jsonFile = `config.json`;
      await new Promise<void>((resolve, reject) => {
        this.http.get(jsonFile).toPromise().then((response: any) => {
            ConfigService.useSetting = response;

            resolve();
        }).catch((response: any) => {
            reject(`Could not load file '${jsonFile}': ${JSON.stringify(response)}`);
        });
      });
    }
    else {
      ConfigService.useSetting = devConfigSetting();
    }
    console.log('主設定', ConfigService.useSetting);
  }
}
