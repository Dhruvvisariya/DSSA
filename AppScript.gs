function doPost(e) {
  var data = e.parameter.data;
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.getRange('A1').setValue(data);

    // Clear contents of Sheet2
  clearSheet2();

  var vid = data; // Assuming 'data' contains the video ID
  scrapeCommentsWithoutReplies(vid);

  return ContentService.createTextOutput("Success");
}

function clearSheet2() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet2 = ss.getSheetByName("Sheet2");
  if (sheet2) {
    sheet2.clear(); // Clear all contents of Sheet2
  }
}

function scrapeCommentsWithoutReplies(vid) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var result = [['Name', 'Comment', 'Time', 'Likes', 'Reply Count']];
  var nextPageToken = undefined;

  while (true) {
    var data = YouTube.CommentThreads.list('snippet', { videoId: vid, maxResults: 100, pageToken: nextPageToken });
    nextPageToken = data.nextPageToken;

    for (var row = 0; row < data.items.length; row++) {
      result.push([
        data.items[row].snippet.topLevelComment.snippet.authorDisplayName,
        data.items[row].snippet.topLevelComment.snippet.textDisplay,
        data.items[row].snippet.topLevelComment.snippet.publishedAt,
        data.items[row].snippet.topLevelComment.snippet.likeCount,
        data.items[row].snippet.totalReplyCount
      ]);
    }

    if (!nextPageToken) {
      break;
    }
  }

  var newSheet = ss.getSheetByName("Sheet2");
  if (!newSheet) {
    newSheet = ss.insertSheet("Sheet2");
  }
  newSheet.getRange(1, 1, result.length, 5).setValues(result);
}
