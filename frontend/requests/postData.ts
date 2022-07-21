export const postData = (data: object, route: string) => {
  fetch(`http://localhost:8080${route}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify(data),
  });
};
