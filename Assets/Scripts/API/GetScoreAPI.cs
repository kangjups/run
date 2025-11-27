/*using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class ScoreAPI : MonoBehaviour
{
    [Header("UI 연결")]
    public TextMeshProUGUI scoreDisplay;     // UI에 보여줄 Text
    public TextMeshProUGUI bestScoreDisplay;
    public TextMeshProUGUI goldDisplay;

    public void GetMyScore()
    {
        // 서버 통신 대신 테스트용 더미 데이터
        ScoreManager.score = Random.Range(0, 100);
        ScoreManager.bestScore = Random.Range(100, 200);
        ScoreManager.totalGold = Random.Range(10, 500);

        UpdateUI();
    }

    private void UpdateUI()
    {
        if (scoreDisplay != null)
            scoreDisplay.text = $"Score : {ScoreManager.score}";

        if (bestScoreDisplay != null)
            bestScoreDisplay.text = $"Best : {ScoreManager.bestScore}";

        if (goldDisplay != null)
            goldDisplay.text = $"Gold : {ScoreManager.totalGold}";
    }
}
*/
/*using UnityEngine;
using UnityEngine.Networking;
using System.Collections;
using UnityEngine.SceneManagement;

public class ScoreAPI : MonoBehaviour
{
    public IEnumerator SendScore(int score)
    {
        string jsonBody = $"{{\"score\": {score}}}";
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(jsonBody);

        using (UnityWebRequest request =
           new UnityWebRequest("http://localhost:5000/score", "POST"))
        {
            request.uploadHandler = new UploadHandlerRaw(bodyRaw);
            request.downloadHandler = new DownloadHandlerBuffer();
            request.SetRequestHeader("Content-Type", "application/json");

            yield return request.SendWebRequest();

            if (request.result == UnityWebRequest.Result.Success)
            {
                Debug.Log("Score Uploaded: " + request.downloadHandler.text);

                // ---------------------------
                // 내려받은 점수 ScoreManager에 저장
                // ---------------------------
                //ScoreManager.score = score;  // 서버에서 다시 주면 그걸 사용
            }
            else
            {
                Debug.LogError("Upload Error: " + request.error);
            }
        }
    }
}
*/