
import { useCallback, useEffect, useState } from "react";
import { getSurveys } from "../api/client";
import DataState from "../components/DataState";

export default function SurveyList({ onSelect }) {
  const [surveys, setSurveys] = useState([]);
  const [keyword, setKeyword] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadSurveys = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const data = await getSurveys();
      setSurveys(Array.isArray(data) ? data : []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadSurveys();
  }, [loadSurveys]);

  const filtered = surveys.filter((survey) =>
    String(survey.SurveyID).includes(keyword.trim()) ||
    String(survey.FullName || "")
      .toLowerCase()
      .includes(keyword.trim().toLowerCase())
  );

  return (
    <section>
      <h2>Danh sách khảo sát CSAT/NPS</h2>

      <label htmlFor="survey-search">
        Tìm khảo sát:
      </label>

      <input
        id="survey-search"
        type="search"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
        placeholder="Nhập mã khảo sát hoặc tên khách hàng"
      />

      <DataState
        loading={loading}
        error={error}
        empty={surveys.length === 0}
        emptyMessage="Chưa có khảo sát nào trong hệ thống."
        onRetry={loadSurveys}
      >
        {filtered.length === 0 ? (
          <p>Không tìm thấy khảo sát phù hợp với từ khóa.</p>
        ) : (
          filtered.map((survey) => (
            <div
              key={survey.SurveyID}
              style={{
                border: "1px solid #ccc",
                padding: 16,
                marginTop: 12,
                borderRadius: 8,
              }}
            >
              <h3>Khảo sát #{survey.SurveyID}</h3>
              <p>Mã phiếu: {survey.TicketID}</p>
              <p>Khách hàng: {survey.FullName}</p>
              <p>Cửa hàng: {survey.StoreName}</p>

              <button
                type="button"
                onClick={() => onSelect(survey.SurveyID)}
              >
                Xem chi tiết
              </button>
            </div>
          ))
        )}
      </DataState>
    </section>
  );
}
