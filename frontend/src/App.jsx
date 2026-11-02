
import { useEffect, useState } from "react";
import {
  getCurrentUser,
  logout,
} from "./api/client";

import Login from "./pages/Login";
import SurveyList from "./pages/SurveyList";
import SurveyDetail from "./pages/SurveyDetail";
import FeedbackForm from "./pages/FeedbackForm";

import "./App.css";

export default function App() {
  const [username, setUsername] = useState(null);
  const [checking, setChecking] = useState(true);
  const [page, setPage] = useState("list");
  const [selectedId, setSelectedId] = useState(null);
  const [authError, setAuthError] = useState("");

  useEffect(() => {
    getCurrentUser()
      .then((data) => setUsername(data.username))
      .catch(() => setUsername(null))
      .finally(() => setChecking(false));
  }, []);

  async function handleLogout() {
    setAuthError("");

    try {
      await logout();
      setUsername(null);
      setPage("list");
      setSelectedId(null);
    } catch (err) {
      setAuthError(`Không thể đăng xuất: ${err.message}`);
    }
  }

  function showDetail(id) {
    setSelectedId(id);
    setPage("detail");
  }

  if (checking) {
    return <p role="status">Đang kiểm tra đăng nhập...</p>;
  }

  if (!username) {
    return <Login onLogin={setUsername} />;
  }

  return (
    <main>
      <h1>Smart CRM – Mekong Mobile</h1>
      <p>Hệ thống khảo sát hài lòng CSAT/NPS</p>

      <p>Đang đăng nhập: <strong>{username}</strong></p>

      <button type="button" onClick={handleLogout}>
        Đăng xuất
      </button>

      {authError && <p role="alert">{authError}</p>}

      <nav>
        <button type="button" onClick={() => setPage("list")}>
          Danh sách khảo sát
        </button>

        <button type="button" onClick={() => setPage("feedback")}>
          Tiếp nhận phản hồi
        </button>
      </nav>

      <hr />

      {page === "list" && (
        <SurveyList onSelect={showDetail} />
      )}

      {page === "detail" && (
        <SurveyDetail
          id={selectedId}
          onBack={() => setPage("list")}
        />
      )}

      {page === "feedback" && <FeedbackForm />}
    </main>
  );
}
