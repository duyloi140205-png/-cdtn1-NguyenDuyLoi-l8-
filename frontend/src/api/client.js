
const API_URL = "/api";

async function request(path, options = {}) {
 const response = await fetch(`${API_URL}${path}`, {
  credentials: "same-origin",
  ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.error || `Lỗi API: ${response.status}`);
  }

  return data;
}

export const getSurveys = () => request("/surveys");

export const getSurvey = (id) =>
  request(`/surveys/${id}`);

export const createSurvey = (data) =>
  request("/surveys", {
    method: "POST",
    body: JSON.stringify(data),
  });

export const submitFeedback = (surveyId, data) =>
  request(`/surveys/${surveyId}/feedback`, {
    method: "POST",
    body: JSON.stringify(data),
  });

export const login = (username, password) =>
  request("/auth/login", {
    method: "POST",
    body: JSON.stringify({ username, password }),
  });

export const getCurrentUser = () =>
  request("/auth/me");

export const logout = () =>
  request("/auth/logout", {
    method: "POST",
  });
