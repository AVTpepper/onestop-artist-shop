function toggleComment(commentId) {
    const contentElement = document.getElementById(`comment-content-${commentId}`);
    const toggleButton = document.getElementById(`toggle-btn-${commentId}`);
    const truncatedContent = contentElement.textContent.slice(0, 64);

    if (toggleButton.textContent === "Show more") {
        contentElement.setAttribute('data-original-content', contentElement.textContent);
        contentElement.textContent = truncatedContent;
        toggleButton.textContent = "Show less";
    } else {
        contentElement.textContent = contentElement.getAttribute('data-original-content');
        toggleButton.textContent = "Show more";
    }
}

// Truncate comments initially
document.addEventListener('DOMContentLoaded', () => {
    const commentElements = document.querySelectorAll('[id^="comment-content-"]');
    commentElements.forEach((element) => {
        const commentId = element.id.split('-').pop();
        toggleComment(commentId);
    });
});