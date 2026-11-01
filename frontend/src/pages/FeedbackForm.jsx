
import { useState } from "react";
import { submitFeedback } from "../api/client";

export default function FeedbackForm() {
  const [surveyId, setSurveyId] = useState("");
  const [csat, setCsat] = useState("5");
  const [nps, setNps] = useState("10");
  const [comment, setComment] = useState("");
  const [message, setMessage] = useState("");
  const [saving, setSaving] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setSaving(true);
    setMessage("");

    try {
      await submitFeedback(Number(surveyId), {
        csat: Number(csat),
        nps: Number(nps),
        comment,
      });

      setMessage("Gửi phản hồi thành công!");
      setComment("");
    } catch (error) {
      setMessage(`Gửi thất bại: ${error.message}`);
    } finally {
      setSaving(false);
    }
  }

  return (
    <section>
      <h2>Tiếp nhận phản hồi CSAT/NPS</h2>

      <form onSubmit={handleSubmit}>
        <p>
          Mã khảo sát:
          <input
            type="number"
            min="1"
            required
            value={surveyId}
            onChange={(e) => setSurveyId(e.target.value)}
          />
        </p>

        <p>
          Điểm CSAT (1–5):
          <input
            type="number"
            min="1"
            max="5"
            required
            value={csat}
            onChange={(e) => setCsat(e.target.value)}
          />
        </p>

        <p>
          Điểm NPS (0–10):
          <input
            type="number"
            min="0"
            max="10"
            required
            value={nps}
            onChange={(e) => setNps(e.target.value)}
          />
        </p>

        <p>
          Nhận xét:
          <textarea
            value={comment}
            maxLength={2000}
            onChange={(e) => setComment(e.target.value)}
          />
        </p>

        <button type="submit" disabled={saving}>
          {saving ? "Đang gửi..." : "Gửi phản hồi"}
        </button>
      </form>

      <p role="status">{message}</p>
    </section>
  );
}
