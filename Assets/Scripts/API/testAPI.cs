/*
using UnityEngine;
using UnityEngine.SceneManagement;

public class Replay : MonoBehaviour
{
    public void ReplayGame()
    {
        GameManager.gameStarted = false;

        SceneManager.LoadScene("PlayScens");
    }

    public void Showscore()
    {
        // 여기다가 api 컨테이너에서 지금까지의 점수를 모두 보여주는 코드
        // 
    }

}
*/
using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections; // <-- 코루틴을 위해 추가
using UnityEngine.Networking; // <-- 웹 요청을 위해 추가
using TMPro; // <-- TextMeshPro 사용을 위해 추가

public class Replay : MonoBehaviour
{
    // 점수 기록을 표시할 TextMeshPro UI
    // 유니티 에디터에서 이 스크립트가 붙은 GameObject에 
    // 점수 표시용 TextMeshPro UI 객체를 연결해주세요.
    public TextMeshProUGUI scoreDisplay;

//core record" 버튼에 이 함수를 연결
    public void Showscore()
    {
        if (scoreDisplay != null)
        {
            scoreDisplay.text = "Loading scores..."; 
        }
        StartCoroutine(GetScoresRoutine());
    }

    IEnumerator GetScoresRoutine()
    {
        using (UnityWebRequest request = UnityWebRequest.Get("http://localhost:5000/scores"))
        {
            yield return request.SendWebRequest();

            string displayText = "";

            if (request.result == UnityWebRequest.Result.Success)
            {
                string jsonResponse = request.downloadHandler.text;
                Debug.Log("Scores received: " + jsonResponse);

                try
                {
                    ScoreApiResponse response = JsonUtility.FromJson<ScoreApiResponse>(jsonResponse);
                    if (response.status == "success")
                    {
                        displayText = "== Top 10 Scores ==\n";
                        if (response.scores.Length == 0)
                        {
                            displayText += "(No scores yet)";
                        }
                        else
                        {
                            foreach (var scoreData in response.scores)
                            {
                                displayText += scoreData.score + "\n";
                            }
                        }
                    }
                    else
                    {
                        displayText = "Failed to load scores.";
                    }
                }
                catch (System.Exception e)
                {
                    displayText = "Error parsing JSON.";
                    Debug.LogError("JSON Parse Error: " + e.Message);
                }
            }
            else
            {
                Debug.LogError("Error fetching scores: " + request.error);
                displayText = "Error: " + request.error;
            }

            if (scoreDisplay != null)
            {
                scoreDisplay.text = displayText;
            }
        }
    }
}


// JSON 파싱을 위한 헬퍼 클래스
[System.Serializable]
public class ScoreApiResponse
{
    public string status;
    public ScoreData[] scores;
}

[System.Serializable]
public class ScoreData
{
    public int score;
}
