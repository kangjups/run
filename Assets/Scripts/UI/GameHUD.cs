using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameHUD : MonoBehaviour
{
    public TextMeshProUGUI scoreText;        // 플레이 씬 실시간 점수
    public TextMeshProUGUI bestScoreText;    // 게임오버 베스트
    public TextMeshProUGUI currentScoreText; // 게임오버 현재 점수
    public TextMeshProUGUI totalScoreText;   // 홈 화면 totalScore

    void Update()
    {
        if (scoreText != null)
            scoreText.text = ScoreManager.Instance.Score.ToString();

        if (bestScoreText != null)
            bestScoreText.text = "Best Score : " + ScoreManager.Instance.BestScore;

        if (currentScoreText != null)
            currentScoreText.text = "Score : " + ScoreManager.Instance.Score;

        if (totalScoreText != null)
            totalScoreText.text = "Gold : " + ScoreManager.Instance.TotalScore;
    }
}
