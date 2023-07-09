export interface ConfigSetting {
  lobby: {
    title: string;
    api: string;
  }
}

export function devConfigSetting(): ConfigSetting {
  " 本地開發統一用 "
  const result = {
    lobby: {
      title: "(本地開發)",
      api: "http://localhost:5000",
      // api: "https://f3ad-124-218-18-117.ngrok-free.app",
    },
  }
  return result;
}
