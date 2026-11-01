
import { useEffect, useState } from "react";
import { getSurvey } from "../api/client";
import DataState from "../components/DataState";

export default function SurveyDetail({ id, onBack }) {
  const [survey, setSurvey] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    getSurvey(id)
      .then(setSurvey)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, [id]);

  return (
    <section>
      <h2>Chi tiết khảo sát</h2>

      <DataState
        loading={loading}
        error={error}
        empty={!survey}
      >
        <p>Mã khảo sát: {survey?.SurveyID}</p>
        <p>Mã phiếu: {survey?.TicketID}</p>
        <p>Khách hàng: {survey?.FullName}</p>
        <p>Trạng thái: {survey?.Status}</p>
      </DataState>

      <button onClick={onBack}>Quay lại</button>
    </section>
  );
}
