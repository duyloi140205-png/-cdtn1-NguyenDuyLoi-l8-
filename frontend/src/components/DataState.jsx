
export default function DataState({
  loading,
  error,
  empty,
  children,
}) {
  if (loading) {
    return <p>Đang tải dữ liệu...</p>;
  }

  if (error) {
    return <p role="alert">Lỗi: {error}</p>;
  }

  if (empty) {
    return <p>Chưa có dữ liệu khảo sát.</p>;
  }

  return <>{children}</>;
}
