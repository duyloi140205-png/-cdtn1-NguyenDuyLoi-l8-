
export default function DataState({
  loading,
  error,
  empty,
  emptyMessage = "Chưa có dữ liệu.",
  onRetry,
  children,
}) {
  if (loading) {
    return <p role="status">Đang tải dữ liệu...</p>;
  }

  if (error) {
    return (
      <div role="alert">
        <p>Lỗi kết nối: {error}</p>
        {onRetry && (
          <button type="button" onClick={onRetry}>
            Thử lại
          </button>
        )}
      </div>
    );
  }

  if (empty) {
    return <p>{emptyMessage}</p>;
  }

  return <>{children}</>;
}
