
$(document).ready(function () {
    // Initial variables
    var currentPage = 1;
    var artworksPerPage = 12;
    var selectedCategoryId = null;

    function paginateArtworks() {
        // Get filtered artworks
        var filteredArtworks = $(".artwork" + (selectedCategoryId ? '[data-category="' + selectedCategoryId + '"]' : ""));

        // Calculate the total number of pages
        var totalPages = Math.ceil(filteredArtworks.length / artworksPerPage);

        // Hide all artworks
        $(".artwork").hide();

        // Show artworks for the current page
        var startIndex = (currentPage - 1) * artworksPerPage;
        var endIndex = startIndex + artworksPerPage;
        filteredArtworks.slice(startIndex, endIndex).show();

        // Update the pagination UI
        updatePaginationUI(totalPages);
    }

    function updatePaginationUI(totalPages) {
        // Clear existing pagination
        $(".pagination").empty();

        // Previous button
        var prevItem = $('<li class="page-item"><a class="page-link" href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>');
        prevItem.click(function (e) {
            e.preventDefault();
            if (currentPage > 1) {
                currentPage--;
                paginateArtworks();
            }
        });
        $(".pagination").append(prevItem);

        // Page range calculation
        var startPage = Math.max(1, currentPage - 1);
        var endPage = Math.min(totalPages, startPage + 2);
        if (endPage - startPage < 2) {
            startPage = Math.max(1, endPage - 2);
        }

        // Add pagination links
        for (var i = startPage; i <= endPage; i++) {
            var pageItem = $('<li class="page-item"><a class="page-link" href="#">' + i + "</a></li>");
            if (i === currentPage) {
                pageItem.addClass("active");
            }
            pageItem.click(function (e) {
                e.preventDefault();
                currentPage = i;
                paginateArtworks();
            });
            $(".pagination").append(pageItem);
        }

        // Next button
        var nextItem = $('<li class="page-item"><a class="page-link" href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>');
        nextItem.click(function (e) {
            e.preventDefault();
            if (currentPage < totalPages) {
                currentPage++;
                paginateArtworks();
            }
        });
        $(".pagination").append(nextItem);
    }

    // Initialize pagination
    paginateArtworks();

    // Category click event
    $('.row.my-5').on('click', 'a.category-link', function (e) {
        e.preventDefault();

        // Remove the grayed-out class from all categories
        $(".category-link").removeClass("grayed-out");

        // Add the grayed-out class to all categories except the clicked one
        $(".category-link").not(this).addClass("grayed-out");

        selectedCategoryId = $(this).data("category");
        var selectedCategoryName = $(this).find('.card-title').text();

        // Reset the current page and update pagination
        currentPage = 1;
        paginateArtworks();

        // Update the heading text
        $('#artworks-heading').text(selectedCategoryName);

        // Show the "Show All" button only when a category is selected
        if (selectedCategoryId) {
            $('#show-all-button').show();
        } else {
            $('#show-all-button').hide();
        }
    });

    // Initialize the "Show All" button as hidden
    $('#show-all-button').hide();

    // Show all products when the "Show All" button is clicked
    $('#show-all-button').on('click', function () {
        selectedCategoryId = null;

        // Remove the grayed-out class from all categories
        $(".category-link").removeClass("grayed-out");

        // Reset the current page and update pagination
        currentPage = 1;
        paginateArtworks();

        $('#artworks-heading').text('Artwork');
        $(this).hide();
    });
});
