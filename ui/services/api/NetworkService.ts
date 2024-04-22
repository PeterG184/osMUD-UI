export type ApiError = {
  status: number;
  message: string;
};

async function handleNetworkError(r: Response): Promise<ApiError> {
  console.log(r);

  let json = await r.json().catch(() => {});
  let message = "Unexpected error occurred";
  if (json != undefined && "status" in json) {
    message = json.status;
  }

  return {
    status: r.status,
    message,
  };
}

class NetworkService {
  async fetch<T>(route: string, method = "GET", body?: object) {
    let response = await fetch(route, {
      method,
      body: body ? JSON.stringify(body) : undefined,
      headers: {
        "content-type": "application/json",
      },
    });

    if (!response.ok) {
      throw await handleNetworkError(response);
    }

    let json: unknown;
    try {
      json = await response.json();
    } catch {
      json = {};
    }

    return json as T;
  }

  async get<T>(route: string) {
    return this.fetch(route, "GET") as T;
  }

  async put<T>(route: string, body: object) {
    return this.fetch(route, "PUT", body) as T;
  }

  async delete<T>(route: string) {
    return this.fetch(route, "DELETE") as T;
  }
}

export default new NetworkService();
