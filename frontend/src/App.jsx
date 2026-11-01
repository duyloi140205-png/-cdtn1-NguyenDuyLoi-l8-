
import { useState } from "react";
import SurveyList from "./pages/SurveyList";
import SurveyDetail from "./pages/SurveyDetail";
import FeedbackForm from "./pages/FeedbackForm";
import "./App.css";

export default function App() {
  const [page, setPage] = useState("list");
  const [selectedId, setSelectedId] = useState(null);

  function showDetail(id) {
    setSelectedId(id);
    setPage("detail");
  }

  return (
    <main>
      <h1>Smart CRM – Mekong Mobile</h1>
      <p>Hệ thống khảo sát hài lòng CSAT/NPS</p>

      <nav>
        <button onClick={() => setPage("list")}>
          Danh sách khảo sát
        </button>

        <button onClick={() => setPage("feedback")}>
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
