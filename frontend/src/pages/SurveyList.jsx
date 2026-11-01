
import { useEffect, useState } from "react";
import { getSurveys } from "../api/client";
import DataState from "../components/DataState";

export default function SurveyList({ onSelect }) {
  const [surveys, setSurveys] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    getSurveys()
      .then((data) => {
        setSurveys(Array.isArray(data) ? data : []);
      })
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return (
    <section>
      <h2>Danh sách khảo sát CSAT/NPS</h2>

      <DataState
        loading={loading}
        error={error}
        empty={surveys.length === 0}
      >
        {surveys.map((survey) => (
          <div
            key={survey.SurveyID}
            style={{
              border: "1px solid #ccc",
              padding: 16,
              marginBottom: 12,
              borderRadius: 8,
            }}
          >
            <h3>Khảo sát #{survey.SurveyID}</h3>
            <p>Mã phiếu: {survey.TicketID}</p>
            <p>Khách hàng: {survey.FullName}</p>
            <p>Trạng thái: {survey.Status}</p>

            <button onClick={() => onSelect(survey.SurveyID)}>
              Xem chi tiết
            </button>
          </div>
        ))}
      </DataState>
    </section>
  );
}
